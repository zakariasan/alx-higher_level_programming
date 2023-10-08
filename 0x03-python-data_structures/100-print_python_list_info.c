#include <Python.h>
#include <stddef.h>
#include <string.h>
/**
 * print_python_list_info - print list infos
 *
 * Return: Always 0.
 */
void print_python_list_info(PyObject *p)
{
	size_t len,i;
	PyListObject *obj_list;
	PyObject *obj;
	
	if (!strcmp(p->ob_base->tp_name, 'list'))
	{
		obj_list = p;
		size = list->ob_base.ob_size;
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", list->Allocated);

		i = 0;
		while (i < size)
		{
			obj = obj_list->ob_item[i]
			printf("Element %ld: %s\n", i, obj->ob_type->tp_name);
			i++;
		}

	}
	
}
