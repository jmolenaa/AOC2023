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

int	find_colour(std::string line, std::string colour, int max_balls)
{
	int	j = 0;

	while (j != std::string::npos)
	{
		j = line.find(colour, j + 1);
		if (j != std::string::npos && weird_atoi(line, j - 2) > max_balls)
			return (0);
	}
	return (1);
}

void read_file(std :: ifstream & fd)
{
	std :: string	line;
	int				i = 1;
	int				count = 0;

	while (getline(fd, line))
	{
		if (find_colour(line, "blue", 14) == 1 && \
			find_colour(line, "green", 13) == 1 && \
			find_colour(line, "red", 12) == 1)
			count += i;
		i++;
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