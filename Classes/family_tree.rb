class Person
  def initialize(name, birth_year, alive=true)
    @name = name
    @birth_year = birth_year
    @alive = alive
  end
  
  def name
    return @name
  end
  
  def birth_year
    return @birth_year
  end
  
  def alive?
    return @alive
  end
  
  def age
    return Time.now.year - self.birth_year
  end
end

if __FILE__==$0
  me = Person.new('Paul', 1986)
  puts me.name
  puts me.birth_year
  puts me.alive?
  puts me.age
end