#include <iostream>
#include <fstream>
#include <string>

int	weird_atoi(std::string line, int j)
{
	int	number = 0;
	int	times = 1;

	while (isdigit(line[j]))
	{
		number = number + (line[j] - '0') * times;
		times = times * 10;
		j--;
	}
	return (number);
}

int	find_minimum_balls(std::string line, std::string colour)
{
	int	j = 0;
	int	minimum = 0;

	while (j != std::string::npos)
	{
		j = line.find(colour, j + 1);
		if (j != std::string::npos && weird_atoi(line, j - 2) > minimum)
			minimum = weird_atoi(line, j - 2);
	}
	return (minimum);
}

void read_file(std :: ifstream & fd)
{
	std :: string	line;
	int				count = 0;

	while (getline(fd, line))
		count += find_minimum_balls(line, "blue") * find_minimum_balls(line, "green") * find_minimum_balls(line, "red");
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