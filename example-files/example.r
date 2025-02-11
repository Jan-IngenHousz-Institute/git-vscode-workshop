# test.R
# This script is designed to test LSP features in R such as syntax checking,
# autocompletion, and inline documentation.

# A recursive function to compute factorial
factorial_recursive <- function(n) {
  if (n < 0) {
    stop("Factorial is not defined for negative numbers.")
  }
  if (n == 0) {
    return(1)
  }
  return(n * factorial_recursive(n - 1))
}

# A function to compute the sum of squares of a numeric vector
sum_of_squares <- function(vec) {
  if (!is.numeric(vec)) {
    stop("Input must be numeric.")
  }
  return(sum(vec^2))
}

# Example of creating and using an S3 class in R
# Define a constructor for a simple Point class
create_point <- function(x, y) {
  point <- list(x = x, y = y)
  class(point) <- "Point"
  return(point)
}

# Define a print method for objects of class "Point"
print.Point <- function(point) {
  cat("Point(", point$x, ", ", point$y, ")\n", sep = "")
}

# Test the functions and S3 class
cat("Factorial of 5:", factorial_recursive(5), "\n")
cat("Sum of squares for c(1, 2, 3, 4):", sum_of_squares(c(1, 2, 3, 4)), "\n")

# Create and print a Point object
pt <- create_point(3, 4)
print(pt)