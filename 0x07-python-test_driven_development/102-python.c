#include <Python.h>

/**
 * print_python_string - function that prints Python strings
 * @p: a string
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t length;
	/* Check if p is a valid object */
	if (!PyUnicode_Check(p))
	{
		printf("[ERROR] Invalid String Object\n");
		return;
	}
	/*get string information*/
	const char *val = PyUnicode_AsUTF8AndSize(p, &length);
	int type = PyUnicode_KIND(p);

	/*print*/
	printf("[.] string object info\n");
	printf(" type: %s\n", type == PyUnicode_1BYTE_KIND
			? "compact ascii" : "compact unicode object");
	printf(" length: %zd\n", length);
	printf(" value: %s\n", val);
}
