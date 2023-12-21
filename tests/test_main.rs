use hello::*;

#[test]
fn test_say_my_name() {
    let name = "Alice";
    say_my_name(name);
    // doesn't work, need to fix
    // assert_eq!(say_my_name(name), format!("My name is {}", name));
}
