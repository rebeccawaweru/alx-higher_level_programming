#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - function to print basic data about the python lists
 * @p: object
 */
void print_python_list(PyObject *p)
{
	const char *kind;
	PyListObject *arry = (PyListObject *)p;
	Py_ssize_t j, loc, sz;
	PyVarObject *val = (PyVarObject *)p;

	loc = arry->allocated;
	sz = val->ob_size;

	fflush(stdout);
	printf("[*] Python list info\n");
	while (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf(" [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", sz);
	printf("[*] Allocated = %ld\n", loc);
	for (j = 0; j < sz; j++)
	{
		kind = arry->ob_item[j]->ob_type->tp_name;
		printf("Element %ld: %s\n", j, kind);
		if (strcmp(kind, "bytes") == 0)
			print_python_bytes(arry->ob_item[j]);
		else if (strcmp(kind, "float") == 0)
			print_python_float(arry->ob_item[j]);
	}
}
/**
 * print_python_bytes - function to print info on byte objects in python
 * @p: the object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *b = (PyBytesObject *)p;
	Py_ssize_t j, sz;

	fflush(stdout);
	printf("[.] bytes object info\n");
	while (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf(" size:%ld\n", ((PyVarObject *)p)->ob_size);
	printf(" trying string: %s\n", b->ob_sval);
	if (((PyVarObject *)p)->ob_size >= 10)
		sz = 10;
	else
		sz = ((PyVarObject *)p)->ob_size + 1;
	printf(" first %ld bytes: ", sz);
	for (j = 0; j < sz; j++)
	{
		printf("%02hhx", b->ob_sval[j]);
		if (j == (sz - 1))
			printf("\n");
		else
			printf(" ");
	}
}
/**
 * print_python_float - function to print data about floating objects
 * @p: the object
 */
void print_python_float(PyObject *p)
{
	char *y = NULL;
	PyFloatObject *x = (PyFloatObject *)p;

	fflush(stdout);
	printf("[.] float object info\n");
	while (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf(" [ERROR] Invalid Float Object\n");
		return;
	}
	y = PyOS_double_to_string(x->ob_fval, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf(" value: %s\n", y);
	PyMem_Free(y);
}
