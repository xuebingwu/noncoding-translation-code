cd /home/xw2629/software/s4pred/
input="N90.30aa.txt"
output="Pep30.structure.fa"
rm $output
i=0
while IFS= read -r line
do
  i=$(( i+1 ))
  echo $i
  echo ">$line$line" > input.fas
  python run_model.py --device gpu --outfmt fas input.fas >> $output
done < "$input"

more Pep30.structure.fa | grep -v ">" | sed -n 1~2p > seq
more Pep30.structure.fa | grep -v ">" | sed -n 2~2p > str
paste seq str > Pep30.30aa.secondary.structure.txt