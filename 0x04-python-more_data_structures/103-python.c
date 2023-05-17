#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - acquire information about pthon objects
 * @p: PyObject pointer
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, j;
	char *s;

	printf("[.] bytes object info\n");
	while (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = (*((PyVarObject *)p)).ob_size;
	s = (*((PyBytesObject *)p)).ob_sval;

	printf(" size: %ld\n", size);
	printf(" trying string: %s\n", s);
	printf(" first %ld bytes:", size + 1 > 10 ? 10 : size + 1);
	for (j = 0; j < size + 1 && j < 10; j++)
		printf(" %.2x", (unsigned char)s[j]);
	putchar('\n');
}

/**
 * print_python_list - python list printing
 * @p: PythonObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, loc, j;
	PyObject *item;

	printf("[*] Python list info\n");
	size = (*((PyVarObject *)p)).ob_size;
	loc = (*((PyListObject *)p)).allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", loc);

	for (j = 0; j < size; j++)
	{
		item = PyList_GET_ITEM(p, j);
		printf("Element %ld: %s\n", j, (*((PyObject *)item)).ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
