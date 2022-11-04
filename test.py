import json

def compute_differences(before, after):
    output = {"added": {}, "removed": {}}
    for k, v in before.items():
        if k not in list(after.keys()):
            output["removed"][k] = sorted(v)
    for k, v in after.items():
        if k not in list(before.keys()):
            output["added"][k] = sorted(v)
        elif v != before[k]:   
            diff1 = list(set(v).difference(set(before[k])))
            if diff1:
                output["added"][k] = sorted(diff1)
            diff2 = list(set(before[k]).difference(set(v)))
            if diff2:
                output["removed"][k] = sorted(diff2)

    sorted_output = {"added": {}, "removed": {}}
    added_keys = sorted(output["added"])
    for key in added_keys:
        sorted_output["added"][key] = output["added"][key]
    removed_keys = sorted(output["removed"])
    for key in removed_keys:
        sorted_output["removed"][key] = output["removed"][key]

    return json.dumps((sorted_output))


before = {
	"Mercedes-Benz": [
		"AMG GT",
		"S-Class"
	],
	"Porsche": [
		"911",
		"Boxster",
		"Roadster"
	],
	"Tesla": [
		"Model S",
		"Model X"
	]
}
after = {
	"Acura": [
		"Integra",
		"RSX"
	],
	"Mercedes-Benz": [
		"Roadster"
	],
	"Porsche": [
		"911",
		"Roadster"
	],
	"Tesla": [
		"Model 3",
		"Model Y"
	]
}

print(compute_differences(before, after))
'''
{
    "added": {
        "Acura": [
            "Integra", 
            "RSX"
        ], 
        "Mercedes-Benz": [
            "Roadster"
        ], 
        "Tesla": [
            "Model 3", 
            "Model Y"
        ]
    }, 
    "removed": {
        "Mercedes-Benz": [
            "AMG GT",
            "S-Class"
        ],
        "Porsche": [
            "Boxster"
        ], 
        "Tesla": [
            "Model S", 
            "Model X"
        ]
    }
}
'''