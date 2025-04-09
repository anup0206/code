
# class TwoDvector:
#     def __init__(self,i,j):
#         self.i = i 
#         self.j = j
#     def show(self):
#         print(f"The two d vector is {self.i}i +{self.j}j")

# class ThreeDvector(TwoDvector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k = k
#     def show(self):
#         print(f"The two d vector is {self.i}i +{self.j}j +{self.k}k")

# m = TwoDvector(1,2)
# m.show()
# n = ThreeDvector(3,4,5)
# n.show()


# class Animals:
#     pass
# class Pets(Animals):
#     pass
# class Dog(Pets):
#     @staticmethod
#     def bark():
#         print(f"bow bow !!")

# a = Dog()
# a.bark()


# class Employee:
#     salary = 90000
#     increment = 20

#     @property
#     def salaryafterincrement(self):
#         return self.salary + self.salary * self.increment / 100

#     @salaryafterincrement.setter
#     def salaryafterincrement(self, new_salary):
#         self.increment = ((new_salary / self.salary) - 1) * 100

# # Using the class
# s = Employee()

# # Accessing the property (getter)
# print(f"Salary after increment: {s.salaryafterincrement}")

# # Setting a new salary (setter)
# s.salaryafterincrement = 108000
# print(f"New increment percentage: {s.increment:.2f}%")

# # Checking again after setting
# print(f"Updated salary after increment: {s.salaryafterincrement}")


# class Complex:
#     def __init__(self, i, j):
#         self.i = i  # Real part
#         self.j = j  # Imaginary part

#     def __add__(self, c2):
#         return Complex(self.i + c2.i, self.j + c2.j)

#     def __mul__(self, c2):
#         # Multiply using complex number formula
#         real_part = self.i * c2.i - self.j * c2.j
#         imag_part = self.i * c2.j + self.j * c2.i
#         return Complex(real_part, imag_part)

#     def __repr__(self):
#         return f"{self.i} + {self.j}i"

# v1 = Complex(1, 2)
# v2 = Complex(3, 4)

# sum_result = v1 + v2
# print("Addition:", sum_result)  # 4 + 6i

# mul_result = v1 * v2
# print("Multiplication:", mul_result)  # -5 + 10i



# class Vector:
#     def __init__(self, values):
#         self.values = values  # store the list of numbers
    
#     def __add__(self, other):
#         # Add each element of self and other
#         result = [a + b for a, b in zip(self.values, other.values)]
#         return Vector(result)

#     def __mul__(self, other):
#         # Dot product: multiply and sum up
#         result = sum(a * b for a, b in zip(self.values, other.values))
#         return result

#     def __repr__(self):
#         return f"Vector({self.values})"

# v1 = Vector([2,4,8])
# v2 = Vector([9,4,6])


# print(v1 + v2)


# print(v1 * v2)



# class Vector3D:
#     def __init__(self, i, j, k):
#         self.i = i
#         self.j = j
#         self.k = k

#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k"

# # Example usage
# v = Vector3D(7, 8, 10)
# print(v)  # Output: 7i + 8j + 10k


class Vector:
    def __init__(self, components):
        self.components = components

    def __len__(self):
        return len(self.components)

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same dimension to add")
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(result)

    def __mul__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same dimension to calculate dot product")
        return sum(a * b for a, b in zip(self.components, other.components))

    def __str__(self):
        return " + ".join(f"{val}e{idx+1}" for idx, val in enumerate(self.components))

# Example usage:
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("v1 =", v1)                       # Output: 1e1 + 2e2 + 3e3
print("v2 =", v2)                       # Output: 4e1 + 5e2 + 6e3
print("Sum =", v1 + v2)                 # Output: 5e1 + 7e2 + 9e3
print("Dot product =", v1 * v2)         # Output: 32
print("Dimension of v1:", len(v1))      # Output: 3

