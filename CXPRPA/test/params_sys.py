import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('The PYTHONPATH is : ' + str(sys.path))
print(sys.argv[1])
