using Raylib_cs;
namespace Testing_raylib_cs_1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");

            Raylib.InitWindow(800, 600, "Raylib Test");

            while (!Raylib.WindowShouldClose())
            {
                Raylib.BeginDrawing();

                Raylib.ClearBackground(Color.Black);
                Raylib.DrawText("Hello", 350, 280, 20, Color.White);
                Raylib.DrawCircle(400, 300, 50, Color.FromHSV(37, 1, 1));

                Raylib.EndDrawing();
            }

            Raylib.CloseWindow();
        }
    }
}
