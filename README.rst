Copying Mock
============

``MagicMock`` has problems when used on a function with mutable arguments.  This is called out in the `documentation <https://docs.python.org/3/library/unittest.mock-examples.html#coping-with-mutable-arguments>`_:

   Another situation is rare, but can bite you, is when your mock is called with mutable arguments. ``call_args`` and ``call_args_list`` store references to the arguments. If the arguments are mutated by the code under test then you can no longer make assertions about what the values were when the mock was called.

They then go on to propose a workaround, using ``side_effect``, but it's not very likable.  There is also an elegant recipe offered which copies arguments at call-time.  It's simply a subclass of ``MagicMock`` which copies the arguments, instead of storing references.  I'm not sure why the recipe wasn't included directly in ``mock``, so here it is as a third-party package.  
