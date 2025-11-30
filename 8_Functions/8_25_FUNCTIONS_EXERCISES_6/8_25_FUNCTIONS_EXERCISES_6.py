"""
8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py.
Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
"""
# from printing_functions import print_items
# requested_copies = ["phone case", "robot toy", "key chain"]
# printed_copies = []
#
# print_items(requested_copies, printed_copies)
# print(requested_copies)
# print(printed_copies)


"""
8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. 
Import the function into your main program file, and call the function using each of these approaches:

import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
"""

# # import module_name
# import computer_builder
# computer_builder.build_computer("ASUS Prime", "Intel i5-13600K", "16GB DDR5")
# computer_builder.build_computer(
#     "MSI MAG Tomahawk",
#     "AMD Ryzen 7 7800X3D",
#     "32GB DDR5",
#     gpu="NVIDIA RTX 4080",  # Goes into additional_parts
#     storage="2TB NVMe SSD",  # Goes into additional_parts
#     cooling="Liquid AIO"  # Goes into additional_parts
# )
#
# server_specs = {
#     "gpu": "Quadro RTX A4000",
#     "network_card": "10Gb Ethernet",
#     "psu": "1200W Platinum",
#     "ups": "APC Smart-UPS"
# }
# computer_builder.build_computer(
#     "Supermicro X13",
#     "Intel Xeon w9-3495X",
#     "128GB ECC RAM",
#     **server_specs
# )

# # from module_name import function_name
# from computer_builder import build_computer
# build_computer(
#     "MSI MAG Tomahawk",
#     "AMD Ryzen 7 7800X3D",
#     "32GB DDR5",
#     gpu="NVIDIA RTX 4080",  # Goes into additional_parts
#     storage="2TB NVMe SSD",  # Goes into additional_parts
#     cooling="Liquid AIO"  # Goes into additional_parts
# )

# # from module_name import function_name as fn
# from computer_builder import build_computer as bc
# bc(
#     "MSI MAG Tomahawk",
#     "AMD Ryzen 7 7800X3D",
#     "32GB DDR5",
#     gpu="NVIDIA RTX 4080",  # Goes into additional_parts
#     storage="2TB NVMe SSD",  # Goes into additional_parts
#     cooling="Liquid AIO"  # Goes into additional_parts
# )


# # import module_name as mn
# import computer_builder as cb
# cb.build_computer(
#     "MSI MAG Tomahawk",
#     "AMD Ryzen 7 7800X3D",
#     "32GB DDR5",
#     gpu="NVIDIA RTX 4080",  # Goes into additional_parts
#     storage="2TB NVMe SSD",  # Goes into additional_parts
#     cooling="Liquid AIO"  # Goes into additional_parts
# )

# # from module_name import *
# from computer_builder import *
# build_computer(
#     "MSI MAG Tomahawk",
#     "AMD Ryzen 7 7800X3D",
#     "32GB DDR5",
#     gpu="NVIDIA RTX 4080",  # Goes into additional_parts
#     storage="2TB NVMe SSD",  # Goes into additional_parts
#     cooling="Liquid AIO"  # Goes into additional_parts
# )

"""
8-17. Styling Functions: Choose any three programs you wrote for this chapter, 
and make sure they follow the styling guidelines described in this section.
"""
