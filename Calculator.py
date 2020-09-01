<?php
	@$user_input = $_POST['txtNumber'];
	@$number = ltrim((string)$user_input, "0");

	$fail=0;
?>

<!-- -->

<!DOCTYPE html>
<html>
<head>
<title>Kaprekar's Constant</title>
<?php require_once "bootstrap.php"; ?>
<style>
body {
  background-image: url("https://images.unsplash.com/photo-1522441815192-d9f04eb0615c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=564&q=80");
  background-color: #c9eeff;
  background-size: cover;
  background-attachment: fixed;
}
div.container {
  color: black;
  padding: 5%;
  margin: 5%;
  background-color: #ffffff;
  border-radius: 30px;
  opacity: 0.8;
}

</style>
</head>
<body>
<div class="container">
<h1 align = "center">Program to verify Kaprekar's Number</h1>
<br>
<h3>Problem Statement: Write a program for constant number 4/5/6 digit</h3>
<p>
6174 is known as Kaprekar's constant for four digits. It is named after the Indian mathematician D. R. Kaprekar. This number is notable for the following rules:
<ol>
<li>Take any four-digit number, using at least two different digits 
(leading zeros are allowed).</li>
<li>Arrange the digits in descending and then in ascending order
to get two four-digit numbers, adding leading zeros if
necessary.</li>
<li>Subtract the smaller number from the bigger number.</li>
<li>Go back to step 2 and repeat.</li>
<li>For further reference: <a href = "https://en.m.wikipedia.org/wiki/6174_(number)">click here</a>.</li>
<ol>
</p>
<p>
</p>
<br><hr><br>
<form method="POST">
<fieldset>
 <legend>Check if a number is a Kaprekar Constant</legend>

<div class="col-md-2"><h4>Enter number:<h4></div> 
 <p></p>
 <div class="col-md-3">
  <INPUT id="txtNumber" placeholder="Example: 1234, 54321" type="text" name="txtNumber" minlength="4" maxlength="6"> </div>
  <button type="submit" class="btn btn-primary">Submit</button>
 </div>
</fieldset>
</form>
<div class="col-md-12">
<fieldset>
 <legend> Result </legend>
<?php
echo "Input from User: " . $user_input . "<br><br>";
if ( $number != (integer)$number ) {
 	echo "Please enter an integer";
	$fail=1;
} elseif ( $number<=1000 or $number>=999999 ) {
	echo "Please enter a number between 1,000 and 9,99,999";
	$fail=1;
}

if ($fail==0){

if (strlen((string)$number)==4)
	{
	echo "This is a four digit number. The Kaprekar's constant for four digits is 6174.<br><br>";
	require "IsKaprekar_4digit.php";
	$answer=IsKaprekar($number);
	echo "<br><b> $answer</b><br>";
	}
if (strlen((string)$number)==5)
	{
	echo "This is a five digit number. There are three series of constants for 5-digit numbers.<br><br>";
	require "IsKaprekar_5digit.php";
	$answer=IsKaprekar($number);
	echo "<br><b> $answer</b><br>";
	}
if (strlen((string)$number)==6)
	{
	echo "This is a six digit number. There are 2 Kaprekar's constants and one series of constants for 6-digit numbers.<br><br>";
	require "IsKaprekar_6digit.php";
	$answer=IsKaprekar($number);
	echo "<br><b> $answer</b><br>";
	}

} else {echo "<h4><b>Error!</b></h4>";}
?>


</fieldset>
</div>
</body>
</html>
