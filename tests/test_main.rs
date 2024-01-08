#[cfg(test)]
mod tests {
    use hello::*;

    #[test]
    fn test_say_my_name() {
        assert_eq!(say_my_name("Alice"), "Hello, Alice!");
    }
}
