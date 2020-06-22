from sys import stdin,stdout

def main():
      stdout.write("Enter the number of elements")
      stdin.readline()

      x = [int(i) for i in stdin.readline().split()]

      summ =0
      stdout.write(str(sum(x)))

if __name__ == "__main__":
      main()
