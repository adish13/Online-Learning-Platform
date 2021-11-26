
#include <FL/Fl.H> // needed in every fltk program
#include <FL/Fl_Window.H> // needed to use the Fl_Window class
#include <FL/Fl_Button.H>
#include <iostream>
using namespace std;

char *int2charstar (int v) {
 char *s = new char[sizeof(int)];
 sprintf(s,"%d",v);
 return s;
};

int main(int argc, char *argv[]) {
    	Fl_Window *window;

window = new Fl_Window (600,600,"DEMO"); // outer window

	Fl_Button *button[16];
	for(int i=1; i<=15; i++)
	{
	button[i-1] = new Fl_Button((1+(i-1)%4)*100,((i-1)/4)*100+100,100,100,int2charstar(i));
	}
	
	button[15] = new Fl_Button(400,400,100,100,"");
	//button[0]->down_color(FL_RED);
	window->color(FL_RED);
	
    	window->end();
    	window->show();
    	
    	int s = Fl::run();// the process waits from here on for events
    	cout<<"exiting...\n";
    	return(s);  
    	
}



