def create_hash_map_from_string(string_name):
    hash_map = {}
    for character in string_name:
        if hash_map.get(character) is None:
            hash_map[character] = 1
        else:
            hash_map[character] += 1
    return hash_map


hash_map_from_string = create_hash_map_from_string('aftab')
print(hash_map_from_string)


def get_non_repeated_first_character(created_hash_map):
    for key, value in created_hash_map.items():
        if value == 1:
            return key


non_repeated_first_character = get_non_repeated_first_character(hash_map_from_string)
print(non_repeated_first_character)
