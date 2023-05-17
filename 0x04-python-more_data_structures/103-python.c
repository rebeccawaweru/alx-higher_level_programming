#include <Python.h>

/**
 * print_python_list - acquire information about Python lists
 * @p: PyObject
 */
void print_python_list(PyObject *p)
{
	const char *charactertype;
	int j, loc, s;
	PyListObject *arry = (PyListObject *)p;
	PyVarObject *val = (PyVarObject *)p;

	s = val->ob_size;
	loc = arry->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", loc);
	for (j = 0; j < s; j++)
	{
		charactertype = arry->ob_item[j]->ob_type->tp_name;
		printf("Element %d: %s\n", j, charactertype);
		while (strcmp(charactertype, "bytes") == 0)
			print_python_bytes(arry->ob_item[j]);
	}
}

/**
 * print_python_bytes - print byte objects in Python
 * @p: PyObject
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *y = (PyBytesObject *)p;
	unsigned char s, j;

	printf("[.] bytes object info\n");
	while (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf(" size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf(" trying string: %s\n", y->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		s = 10;
	else
		s = ((PyVarObject *)p)->ob_size + 1;
	printf(" first %d bytes: ", s);
	for (j = 0, j < s; j++)
	{
		printf("%02hhx", y->ob_sval[j]);
		if (j == (s - 1))
			printf("\n");
		else
			printf(" ");
	}
}
