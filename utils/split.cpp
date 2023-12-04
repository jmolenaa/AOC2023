#include <iostream>
#include <vector>

std::vector<std::string>	split_on_word(std::string str, std::string delim)
{
	std::vector<std::string>	split_word;
	size_t						s_pos = 0;
	size_t						e_pos = 0;

	while ((e_pos = str.find(delim, s_pos)) != std::string::npos)
	{
		if (e_pos != s_pos)
			split_word.push_back(str.substr(s_pos, e_pos - s_pos));
		s_pos = e_pos + delim.length();
	}
	split_word.push_back(str.substr(s_pos));
	return (split_word);
}

std::vector<std::string>	split_on_chars(std::string str, std::string delim)
{
	std::vector<std::string>	split_word;
	size_t						s_pos = str.find_first_not_of(delim, 0);
	size_t						e_pos = 0;

	while (s_pos != std::string::npos && (e_pos = str.find_first_of(delim, s_pos)) != std::string::npos)
	{
		split_word.push_back(str.substr(s_pos, e_pos - s_pos));
		s_pos = str.find_first_not_of(delim, e_pos);
	}
	if (s_pos != std::string::npos)
		split_word.push_back(str.substr(s_pos));
	return (split_word);
}

// int	main(int argc, char *argv[])
// {
// 	std :: vector<std::string>	split_word;

// 	(void)argc;
// 	split_word = split_on_word(argv[1], " ");
// 	for (std::string str : split_word)
// 		std::cout << str << "\n";
// 	std::cout << split_word.capacity() << "\n";
// 	std::cout << "On chars\n";
// 	split_word = split_on_chars(argv[1], ": ");
// 	for (std::string str : split_word)
// 		std::cout << "|" << str << "|\n";
// 	// split_word.resize(1);
// 	std::cout<<split_word.capacity() << "\n";
// 	// for (std::string str : split_word)
// 		// std::cout << "|" << str << "|\n";
// 	return (0);


// }
