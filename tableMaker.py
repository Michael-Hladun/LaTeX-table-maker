# reads in spreadsheet values copied to terminal and creates LaTeX table

print("Please copy and paste your spreadsheet data. Hit enter, ctrl-D when done.\n")

lines = []
try:
    while True:
        lines.append(input())
except EOFError:
    pass

lines = [lines[i]+r"\\"+"\n" for i in range(len(lines)-1)]
columns = len(lines[0].split("\t"))
lines = [x.replace("\t", "  &  ") for x in lines]
lines = ["\t"+lines[i] for i in range(len(lines))]

placement = [columns]
placement = ["c" for x in range(columns)]
placement = " ".join(placement)

print("Here is your table:\n")

print(
r'''\begin{table}[H]
	\centering
	\begin{tabular}{'''+placement+r'''}
'''+"".join(lines)+r'''	\end{tabular}
	\caption{CaptionHere}\label{LabelMe}
\end{table}
\medskip''')
