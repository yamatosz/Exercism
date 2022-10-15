from list_methods import (
                        add_me_to_the_queue,
                        find_my_friend,
                        add_me_with_my_friends,
                        remove_the_mean_person,
                        how_many_namefellows,
                        remove_the_last_person,
                        sorted_names,
                        )

print(add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=1, person_name="RichieRich"))
print(add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=0, person_name="HawkEye"))
print(find_my_friend(queue=["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], friend_name="Steve"))
print(add_me_with_my_friends(queue=["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], index=1, person_name="Bucky"))
print(remove_the_mean_person(queue=["Natasha", "Steve", "Eltran", "Wanda", "Rocket"], person_name="Eltran"))
print(how_many_namefellows(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"], person_name="Natasha"))
print(remove_the_last_person(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"]))
print(sorted_names(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"]))
