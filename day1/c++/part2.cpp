#include <iostream>
#include <fstream>

int find_word(std::string line, int i)
{
	std :: string 	numbers[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
	int index = 0;

	for (std::string number : numbers)
	{
		if (line.compare(i, number.length(), number) == 0){
			return (index + 1);
		}
		index++;
	}
	return (-1);
}

int find_reverse_word(std::string line, int i)
{
	std :: string 	numbers[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
	int index = 0;

	for (std::string number : numbers)
	{
		// checks so we don't use negative index for line.compare (we use i - number.length)
		if ((size_t)i < number.length()){
			index++;
			continue;
		}
		if (line.compare(i - number.length(), number.length(), number) == 0){
			return (index + 1);
		}
		index++;
	}
	return (-1);
}

int find_digit(std::string line)
{
	int 	digit = -1;

	for (int i = 0; line[i]; i++)
	{
		if (isdigit(line[i]))
			return (line[i] - '0');
		digit = find_word(line, i);
		if (digit != -1)
			return (digit);
	}
	return (-1);
}

int find_last_digit(std::string line)
{
	int digit = -1;

	for (int i = line.length(); i >= 0; i--)
	{
		if (isdigit(line[i]))
			return (line[i] - '0');
		digit = find_reverse_word(line, i);
		if (digit != -1)
			return (digit);
	}
	return (-1);
}

void    read_file(std :: ifstream & fd){
	std :: string	line;
	int				count = 0;
	int 			digit;

	while (getline(fd, line))
	{
		digit = find_digit(line);
		count += digit * 10;
		digit = find_last_digit(line);
		count += digit;
    }
	std :: cout << count << "\n";
}

int     main(int argc, char *argv[])
{
    std :: ifstream fd;
    std :: string lien;

    if (argc == 1){
        std :: cout << "Please enter the file you want to use as an argument\n";
        return (1);
    }
    fd.open(argv[1]);
    if (!fd){
        std :: cout << "Please enter valid file\n";
        return (1);
    }
    read_file(fd);
}