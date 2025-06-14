mod player;
mod team;

fn main() {
    let mut team = team::create();
    team.roster[0] = player::create_player("Justin Jefferson", 18, 92, 0, 65, 99, 0, 0, 0, 55);
    println!("{}", team);
    for e in team.roster {
        println!("{e}");
    }
}
