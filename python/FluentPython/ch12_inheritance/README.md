## Chapter12 Inheritance: For Good or For Worse

### Subclassing Buit-In Types Is Tricky
Method delegation with the C language Implementation of the built-in type could make trouble with subclass.

### Multiple Inherittance and Method Resolution Order
By checking MRO we can check order of implementation method order. 

### Comping with Multiple Inheritance
#### 1. Distiguish Interface Inheritance from Implemenatation Inheritance
- The main reason for subclassing are
    - Inheritance of interface create a subtype implying "is-a" relationship.
    - Inheritance of implemenation avoids code duplicate by reuse.

#### 2. Make Interfaces explicit with ABCs
#### 3. Use Mixin for Code Reuse
- Mixin class does not define a new type. It merly bundles methods for reuse.
#### 4. Make Mixins Explicit by Naming
There is no formal way in python to state that class is a mixin, so it is recommaned to named with a...Mixin suffix.
#### 5. AN ABC May Also Be a Mixin; The Reverse Is Not True.
#### 6. Don't Subclass from More than One Concrete Class.
One restriction applies to ABCs and not to mixins: The concrete methods implmented in an ABC should only collaborate with methods of the same ABC and its uperclasses.
#### 7. Provide Aggregate Classes to Users.
If some combination of ABCs or mixins is particularly useful to client code. provide a class that brings them together in a sensible way.

