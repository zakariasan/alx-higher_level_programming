#include "Python.h"
#include <stddef.h>

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", ((PyASCIIObject *)(p))->length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &(((PyASCIIObject *)(p))->length)));
}
