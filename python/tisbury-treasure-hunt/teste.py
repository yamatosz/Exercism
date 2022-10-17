from tuples import get_coordinate, convert_coordinate, compare_records, create_record, clean_up

print(get_coordinate(('Scrimshawed Whale Tooth', '2A')))
print(convert_coordinate("2A"))
print(compare_records(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'blue')))
print(compare_records(('Model Ship in Large Bottle', '8A'), ('Harbor Managers Office', ('8', 'A'), 'purple')))
print(create_record(('Brass Spyglass', '4B'), ('Abandoned Lighthouse', ('4', 'B'), 'Blue')))
print(create_record(('Brass Spyglass', '4B'), (('1', 'C'), 'Seaside Cottages', 'blue')))
print(clean_up((('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'), ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'), ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple'))))