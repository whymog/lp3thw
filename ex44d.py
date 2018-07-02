# Defines a class Parent with three methods
class Parent(object):

    # Defines the override() method, which accepts self as an arg
    def override(self):
        # Prints a string
        print("PARENT override()")

    # Defines the implicit() method, which accepts self as an arg
    # This method will not be overridden or altered
    def implicit(self):
        # Prints a string
        print("PARENT implicit()")

    # Defines the altered() method, which accepts self as an arg
    # This method will be invoked using super() within the child
    def altered(self):
        # Prints a string
        print("PARENT altered()")

# Defines a class Child that inherits from Parent
class Child(Parent):

    # Defines a new override() method for Child, which overrides
    # the override() method within Parent
    def override(self):
        # Prints a string
        print("CHILD override()")

    # Defines a new altered() method for Child, which overrides
    # the altered() method within Parent. However, it also
    # invokes its parent class's altered() method using super()
    def altered(self):
        # Prints a string
        print("CHILD, BEFORE PARENT altered()")
        # Calls the altered() method on Child's parent class, Parent
        super(Child, self).altered()
        # Prints another string
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
