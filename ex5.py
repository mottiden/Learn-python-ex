my_name = 'Jesus'
my_age = 33  # not a lie
my_height = 180.0  # cm
my_weight = 80.0  # kg
my_eyes = 'blue'
my_teeth = 'white'
my_hair = 'brown'

print "Let's talk about %s." % my_name
print "He is %d cm tall." % my_height
print "He is %d kilos heavy." % my_weight
print "He is got %s eyes and %s hair" % (my_eyes, my_hair)
print "His teeth are totally %s." % my_teeth

print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

my_weight_pounds = my_weight * 2.205
my_height_inches = my_height * 0.394

print "After the conversion"
print "He is %d heavy and %d tall" % (my_weight_pounds, my_height_inches)
