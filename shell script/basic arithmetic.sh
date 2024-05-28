echo "Enter the first number:"
read num1
echo "Enter the second number:"
read num2

sum=$((num1 + num2))
diff=$((num1 - num2))
prod=$((num1 * num2))

if [$num2 -ne 0]; then
    div=$((num1 / num2))
else 
    div="undefined"

fi

echo "Sum: $sum"
echo "Difference: $diff"
echo "Product: $prod"
echo "Division: $div" 