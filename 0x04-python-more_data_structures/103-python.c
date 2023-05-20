#include <Python.h>
#include <bytesobject.h>
#include <listobject.h>

/**
 *print_python_bytes - parses byteobjects
 *@p: object to parse
 *
 *Return: Nothing
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	char *str;
	int i;

	if (p)
	{
		printf("[.] bytes object info\n");
		if (PyBytes_Check(p))
		{
			PyBytes_AsStringAndSize(p, &str, &size);
			printf("  size: %zd\n", size);
			printf("  trying string: %s\n", str);
			if (size < 10)
				printf("  first %lu bytes: ", size + 1);
			else
				printf("  first 10 bytes: ");
			for  (i = 0; size; i++)
			{
				if (i > 9)
					break;
				printf("%02hhx ", str[i]);
				size--;
			}
			if (i < 9)
				printf("00");
			printf("\n");
		}
		else
			printf("  [ERROR] Invalid Bytes Object\n");
	}
}

/**
 *print_python_list - parses and prints list object
 *@p: listobject
 *
 *Return: Nothing
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	const char *typename;
	PyListObject *listObj = (PyListObject *)p;
	PyObject *item, *type, *name;

	if (p)
	{
		if (PyList_Check(p))
		{
			printf("[*] Python list info\n");
			size = PyList_GET_SIZE(p);
			printf("[*] Size of the Python List = %zd\n", size);
			alloc = listObj->allocated;
			printf("[*] Allocated = %zd\n", alloc);
			if (size)
			{
				for (i = 0; i < size; i++)
				{
					item = PyList_GET_ITEM(p, i);
					type = PyObject_Type(item);
					name = PyObject_GetAttrString(type, "__name__");
					typename = PyUnicode_AsUTF8(name);
					printf("Element %zd: %s\n",i, typename);
					if (!strcmp(typename, "bytes"))
						print_python_bytes(item);

				}
			}
		}
	}

}
