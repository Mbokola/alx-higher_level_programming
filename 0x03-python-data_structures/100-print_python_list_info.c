#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - function that prints a python list
 * @p: pointer to a python list
 *
 *Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *element, *list = (PyListObject *) p;
	long int i = 0;

	printf("[*] Size of the Python List = %ld\n", Py_SIZE(list));
	printf("[*] Allocated =  %ld\n", list->allocated);
	while (i < Py_SIZE(list))
	{
		element = (PyListObject *)PyList_GetItem(p, i);
		printf("Element %ld = %s\n", i, Py_TYPE(element)->tp_name);
		i++;
	}
}
