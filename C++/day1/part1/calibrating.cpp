#include <iostream>
#include <fstream>

void    read_file(std :: ifstream & fd){
	std :: string	line;
	int				count = 0;

	while (getline(fd, line)) {
		count += (line[line.find_first_of("123456789")] - '0') * 10;
		count += (line[line.find_last_of("123456789")] - '0');
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