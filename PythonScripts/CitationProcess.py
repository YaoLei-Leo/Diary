##To process the citation format of md file.
import re

def changeCitationFormat(input_md, output_md):
    output = open(output_md,'w')
    with open(input_md) as f:
        reference_dict=dict()
        for line1 in f:
            if re.search(r'# References:', line1):
                n = 0
                for line2 in f:
                    if re.search(r'\[\^.+_.+_\d+\]', line2) and re.search(r'\[\^.+_.+_\d+\]', line2).group() not in reference_dict:
                        n += 1
                        reference_dict[re.search(r'\[\^.+_.+_\d+\]', line2).group()] = [n, line2]

    with open(input_md) as f:
        for line1 in f:
            if re.search(r'# References:', line1):
                output.write(line1)
                break
            else:
                for i in reference_dict:
                    line1 = line1.replace(i, "[{}]".format(reference_dict[i][0]))
                output.write(line1)

        for i in reference_dict:
            reference_dict[i][1] = reference_dict[i][1].replace(i,"").replace(": ","")
            output.write("[{}] {}".format(reference_dict[i][0], reference_dict[i][1]) + "\n")


changeCitationFormat("./LeoNote/MitochondrialGenetics_raw.md", "./LeoNote/MitochondrialGenetics.md")
                    

