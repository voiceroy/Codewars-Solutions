fn html_special_chars(html: &str) -> String {
    return String::from(html)
        .replace('&', "&amp;")
        .replace('<', "&lt;")
        .replace('>', "&gt;")
        .replace('"', "&quot;");
}
