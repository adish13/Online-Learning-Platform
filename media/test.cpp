#include <SFML/Graphics.hpp>
#include <SFML/Window.hpp>
#include <SFML/OpenGL.hpp>
#include <iostream>
using namespace std;

        bool isSpriteHover(sf::FloatRect sprite, sf::Vector2f mp) 
        {
                if (sprite.contains(mp)){
                return true;
                }
                return false;
        }


int main()
{       

        sf::RenderWindow window, window2, window3;
                window.create(sf::VideoMode(1000, 600),"My first Visual Studio window!");
        
        sf::Texture texture;
        if(!texture.loadFromFile("blue2.png",sf::IntRect(10,10,20,200)))
        {
                return 1;
        }
        sf::Sprite sprite;
        sprite.setTexture(texture);

        sf::Vector2f mp;
    mp.x = sf::Mouse::getPosition(window).x;
    mp.y = sf::Mouse::getPosition(window).y;

        while(window.isOpen())
        {
                sf::Event event;
                
                while(window.pollEvent(event))
                {
                        if(event.type == sf::Event::Closed)
                                window.close();                 
                
                        if(isSpriteHover(sprite.getGlobalBounds(), sf::Vector2f(event.mouseButton.x, event.mouseButton.y)) == true)
         {
                if(event.type == sf::Event::MouseButtonReleased &&  event.mouseButton.button == sf::Mouse::Left)
                {
                        window.create(sf::VideoMode(400, 200),"The button worked!");
                }
         }
         if (event.type == sf::Event::KeyPressed)
{
    if (event.key.code == sf::Keyboard::E)
    {
        std::cout << "the e key was pressed" << std::endl;
    }
}
        
             }
                //window.clear(sf::Color::Black);

                sprite.setPosition(sf::Vector2f(200, 300));
                
                window.draw(sprite);
                
                window.display();

}
        
return 0;
}