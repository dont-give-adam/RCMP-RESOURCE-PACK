from pathlib import Path

directory = Path(r"C:\Users\Minec\AppData\Roaming\.minecraft\resourcepacks\RCMP RESOURCE PACK\assets\scoops_inc\textures\customer\satisfaction")

filenames = []

for file in directory.glob("*.png"):
    filenames.append(int(file.name.rstrip(".png")))

filenames.sort()
print(filenames)

# now we have each filename in asc order stored in filenames



customer_satisfaction_directory = Path(r"C:\Users\Minec\AppData\Roaming\.minecraft\resourcepacks\RCMP RESOURCE PACK\assets\scoops_inc\font\customer_satisfaction.json")

with open(customer_satisfaction_directory,"w") as file:
    file.write('{\n')
    file.write('   "providers":\n')
    file.write('        [\n')



    for image in filenames:
        file.write(f'           {{"type":"bitmap","file":"scoops_inc:customer/satisfaction/{image}.png","ascent":32,"height":32,"chars":["\\uF{str(image).zfill(3)}"]}},\n')


    file.write('        ]\n')
    file.write('}')









#{
#    "providers":
#        [
#            {"type":"bitmap","file":"scoops_inc:customer/satisfaction/1","ascent":400,"height":400,"chars":["\u0001"]}
#
#        ]
#}