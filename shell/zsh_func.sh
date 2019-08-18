#!/bin/zsh
# a function to double a value

db1() {
		value=$(( $1 * 2 ))
		return $value
}
