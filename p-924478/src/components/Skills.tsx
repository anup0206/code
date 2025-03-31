
import React, { useRef, useEffect } from 'react';
import { CheckCircle2, Code2, Globe, Laptop, BookOpen } from 'lucide-react';

interface SkillCategory {
  title: string;
  icon: React.ReactNode;
  skills: string[];
}

const skillCategories: SkillCategory[] = [
  {
    title: "Programming Languages",
    icon: <Code2 className="h-6 w-6 text-primary" />,
    skills: ["HTML5", "CSS", "JavaScript", "Python", "C", "Java"]
  },
  {
    title: "Web Development",
    icon: <Globe className="h-6 w-6 text-primary" />,
    skills: ["Responsive Design", "Frontend Development", "Web APIs", "UI/UX Basics"]
  },
  {
    title: "Tools & Technologies",
    icon: <Laptop className="h-6 w-6 text-primary" />,
    skills: ["Git", "GitHub", "VS Code", "Command Line", "Chrome DevTools"]
  },
  {
    title: "Learning",
    icon: <BookOpen className="h-6 w-6 text-primary" />,
    skills: ["Problem Solving", "Data Structures", "Algorithms", "Object-Oriented Programming"]
  }
];

const SkillCard = ({ category, index }: { category: SkillCategory; index: number }) => {
  const cardRef = useRef<HTMLDivElement>(null);
  
  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          cardRef.current?.classList.add('animate-fade-in');
          observer.unobserve(entry.target);
        }
      },
      { threshold: 0.1 }
    );
    
    if (cardRef.current) {
      observer.observe(cardRef.current);
    }
    
    return () => {
      if (cardRef.current) {
        observer.unobserve(cardRef.current);
      }
    };
  }, []);
  
  return (
    <div 
      ref={cardRef}
      className="glass-card rounded-xl p-6 opacity-0"
      style={{ animationDelay: `${index * 100}ms` }}
    >
      <div className="flex items-center gap-3 mb-4">
        {category.icon}
        <h3 className="text-xl font-semibold">{category.title}</h3>
      </div>
      
      <ul className="space-y-2">
        {category.skills.map((skill, idx) => (
          <li key={idx} className="flex items-center gap-2">
            <CheckCircle2 className="h-4 w-4 text-primary/80" />
            <span>{skill}</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

const Skills = () => {
  return (
    <section id="skills" className="section-container bg-secondary/50">
      <div className="text-center max-w-3xl mx-auto mb-16">
        <h2 className="heading-lg mb-4">My Skills</h2>
        <p className="subheading mx-auto">
          Here are the technologies and skills I've been learning and working with.
          I'm constantly expanding my knowledge in these areas.
        </p>
      </div>
      
      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
        {skillCategories.map((category, index) => (
          <SkillCard key={category.title} category={category} index={index} />
        ))}
      </div>
    </section>
  );
};

export default Skills;
