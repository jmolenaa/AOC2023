#ifndef SPLIT_HPP
# define SPLIT_HPP

# include <vector>
# include <iostream>

std::vector<std::string>	split_on_word(std::string str, std::string delim);
std::vector<std::string>	split_on_chars(std::string str, std::string delim);

#endif