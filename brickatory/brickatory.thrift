namespace py brickatory

typedef i32 int // We can use typedef to get pretty names for the types we are using

/*
	STATE_BALL_IN_PADDLE = 0
	STATE_PLAYING = 1
	STATE_WON = 2
	STATE_GAME_OVER = 3
*/

struct PlayerState
{
	1:string name,
	2:int state
}


service BrickatoryService
{
	int join(1:string name, 2:int brick_width, 3:int brick_height, 4:int paddle_width, 5:int paddle_height, 6:int ball_radius),
        void report(1:PlayerState state),
        list<PlayerState> status()
}
