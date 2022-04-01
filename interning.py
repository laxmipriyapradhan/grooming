"""
1. Shared objects are ranges and specific instances of certain immutable types that CPython instantiates and loads in memory every 
    time a Python interactive session is initialised (Python pre-allocates). These objects are static global variables that can be 
    accessed by all programs executed in a given Python session.

2. The idea behind this implementation is that certain data values are used most often in programming. 
    By always and immediately caching these commonly-used objects, the CPython virtual machine saves significant time and memory. 
    Instead of unnecessarily creating a new object every time one of these values is called, variables can simply be referred 
    to a pre-existing shared object.

3. For integers, the range -5 to 256, included, are loaded as shared objects.

4. Empty tuples are loaded into cache.

5. When Python is instructed to create a reference to an object, it first checks its mutability. 
    If the object is mutable, it will immediately allocate a new object for the value — mutable objects must have unique identities.

6. If the object is immutable, Python will check if the given object matches any shared objects already cached in memory. 
    In the case that a shared object is matched, the variable is directly referred to that pre-allocated object.
    Otherwise, a new object is created.

7. CPython loads the Latin-1 range of characters unicode decimals 0 to 255, inclusive, as shared objects every time Python is initialised. 
    Any calls to values in this range are referred to those pre-existing objects.
"""