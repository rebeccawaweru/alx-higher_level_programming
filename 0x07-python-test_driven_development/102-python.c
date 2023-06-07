#include "Python.h"

/**
 * print_python_string - function that prints Python strings
 * @p: a string
 */
void print_python_string(PyObject *p)
{
	long int ln;

	fflush(stdout);
	printf("[.] string object info\n");

	/* Check if p is a valid object */
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	/*get string information*/
	ln = ((PyASCIIObject *)(p))->length;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", ln);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &ln));
}
