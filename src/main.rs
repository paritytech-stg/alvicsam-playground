#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
    fn perimeter(&self) -> u32 {
        2 * self.width + 2 * self.height
    }
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
impl Rectangle {
    fn square(size: u32) -> Rectangle {
        Rectangle {
            width: size,
            height: size,
        }
    }
}
fn main() {
    let rec1 = Rectangle {
        width: 30,
        height: 50,
    };
    let rec2 = Rectangle {
        width: 20,
        height: 20,
    };
    let _sq = Rectangle::square(3);

    println!("Area of {:?} = {}", rec1, rec1.area());
    println!("Perimeter of {:?} = {}", rec1, rec1.perimeter());
    println!("Rec1 can hold Rec2: {}", rec1.can_hold(&rec2));
}
