# test text_utils  ... strang.py


# if False:  # * --------------------------------- Tests

#     tmp_list1: List[str] = [
#         "this is a-test",
#         "123_456 789-111",
#         "(361) 773-2832",
#         ";alskjdfpo82jn sdf83nf ",
#     ]

#     tmp_whitespace: List[str] = [
#         "  spaces all      over   the    \n places     \t",
#         "white\t\n\r\x0b\x0cspace",
#         "   fasdf   ",
#         "a   b  c     d  e f g hij k  ",
#     ]

#     tmp_list: List[str] = []
#     tmp_list.extend(tmp_whitespace)

#     for i in range(20):
#         tmp_list.append(random_string(25))

#     s: Strang = Strang()
#     re_delimiter = r"[\s-]"
#     delimiter = r" -"
#     print()
#     for item in tmp_list:
# print("---------------------------------")
# print(item)
# print("---------------------------------")
# s = Strang(item)
# print("s:        ", s)
# print("repr:     ", repr(s))
# print("split:    ", s.split_it())
# print("sub:      ", s.sub_it())
# print("upper:    ", s.to_upper_case)
# print("lower:    ", s.to_lower_case)
# print("title:    ", s.to_title_case)
# print("snake:    ", s.to_snake_case)
# print("kebab:    ", s.to_kebab_case)
# print("camel:    ", s.to_camel_case)
# print("pascal:   ", s.to_pascal_case)
# print("clear:    ", s.clear_all_whitespace())
