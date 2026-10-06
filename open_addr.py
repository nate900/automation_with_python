import webbrowser, sys

# google maps: https://www.google.com/maps/place/3323+Talking+Rock+Rd,+Talking+Rock,+GA+30175/@34.4986242,-84.4755508,17z/data=!3m1!4b1!4m6!3m5!1s0x885f8f190d4125b7:0x31d02b1b460b3ef!8m2!3d34.4986198!4d-84.4729759!16s%2Fg%2F11cshmk_dd?entry=ttu&g_ep=EgoyMDI2MDkyMy4wIKXMDSoASAFQAw%3D%3D
# open street map: https://www.openstreetmap.org/search?query=3323+Talking+Rock+rd&zoom=17&minlon=-84.47713851928711&minlat=34.49611448762287&maxlon=-84.46769714355469&maxlat=34.5035063451706#map=19/34.498547/-84.472758
if len(sys.argv) > 1:
    address = '+'.join(sys.argv[1:])
    # webbrowser.open('https://www.openstreetmap.org/search?query=' + address)
    webbrowser.open('https://www.google.com/maps/place/' + address)
    print(address)