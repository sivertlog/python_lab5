# Lab 05
by Sivert Log
### Lab Notes:

***Part One***  
Part one of the lab is located in **py_lab05_p1.py**.
I added `is_bin_part()` and `is_valid_bin_ip()` here as part of the extra credit.
I also added `IndexError` to the *except clause* to catch leading periods.

***Part Two***  
Part two of the lab is located in **py_lab05_p2.py**.

***Part Three***  
Part three of the lab is located in **ip_conversion.py** and **py_lab05_p1.py**.  

*py_lab05_p1.py*  
- `is_bin_part()`checks if the address part contains an eight digit number in binary notation.
I found this detection approach using the `count()` method on [this geeksforgeeks.org page](https://www.geeksforgeeks.org/python-check-if-a-given-string-is-binary-string-or-not/).
- `is_valid_bin_ip()` checks if the binary IP address is valid.
It checks for binary using `is_bin_part()`, then checks for a valid IP part using `binary_to_decimal()` with `is_valid_part()`.

*ip_conversion.py*
- `binary_to_ip()` converts the IP address from binary to decimal
using `binary_to_decimal()` on each address part.
- `ip_to_binary()` converts the IP address from decimal to binary
using `decimal_to_binary()` on each address part. This is also where the leading zero's
are added to make each part 8 bits.
-  `ip_convert()` calls `is_valid_ip()` and `is_valid_bin_ip()`
to detect what type of address is in the string, then calls `ip_to_binary()`
and `binary_to_ip()` respectively for the conversion. If neither is detected, the string `***Invalid IP Address***`
is returned.