#include <iostream>
#include <cstdint>

uint64_t multiply(uint64_t a, uint64_t b) {
    return a * b;
}

uint64_t xor_with_byte(uint64_t a, uint8_t b) {
    return a ^ b;
}

uint64_t hash(const std::string& input) {
    const uint64_t _offset_basis = 0xcbf29ce484222325;
    const uint64_t _prime = 0x100000001b3;
    
    uint64_t hash = _offset_basis;
    
    for (char c : input) {
        hash = multiply(hash, _prime);
        hash = xor_with_byte(hash, static_cast<uint8_t>(c));
    }
    
    return hash;
}

int main() {
    const uint64_t target_hash = 0x80808080808080;
    
    std::cout << "Enter the secret key " << ":\n";
    
    try {
        std::string hex_input;
        std::cin >> hex_input;
        
        std::string bytes;
        for (size_t i = 0; i < hex_input.size(); i += 2) {
            std::string byte_str = hex_input.substr(i, 2);
            char byte = static_cast<char>(std::stoi(byte_str, nullptr, 16));
            bytes.push_back(byte);
        }
        
        const uint64_t result = hash(bytes);
        
        if (result == target_hash) {
            std::cout << "Well done!\nFlag: " 
                      << std::getenv("FLAG") << std::endl;
        } else {
            std::cout << "Try again... :(\n";
        }
        
    } catch (const std::exception& e) {
        std::cerr << "Invalid input: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}