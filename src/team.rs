/*
* The Team module will seek to create and manager our team. This will have
* The team names, location, roster, prestige
*/

use std::fmt;
use crate::player::{Player, create_base_roster};

pub struct Team {
    name: &'static str,
    city: &'static str,
    state: &'static str,
    prestige: i8,
    pub roster: [Player; 10],
}

pub fn create() -> Team {
    let team = Team {
        name: "Generic Team",
        city: "Nowhereville",
        state: "Nil",
        prestige: 0,
        roster: create_base_roster()
    };

    team
}

impl std::fmt::Display for Team {
    fn fmt(&self, fmt: &mut std::fmt::Formatter<'_>) -> fmt::Result {
        write!(fmt, "Team: {}, ({}, {}), {}",
        self.name, self.city, self.state, self.prestige)
    }
}
