int makeNegative(int num)
{
  int negative;
  if (num >= 0) {
      negative = num * (-1);
  } else {
    negative = num;
  }
  
  return negative;
}
