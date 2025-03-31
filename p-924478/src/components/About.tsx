
import React from 'react';

const About = () => {
  return (
    <section id="about" className="section-container">
      <div className="max-w-4xl mx-auto">
        <h2 className="heading-lg mb-8 text-center">About Me</h2>
        
        <div className="grid md:grid-cols-2 gap-12 items-center">
          <div className="space-y-6">
            <p className="text-lg">
              Hello! I'm Anupam Baral, currently pursuing my Bachelor's degree (2023 to present) 
              at Butwal Kalika Campus, Butwal, affiliated with Tribhuvan University.
            </p>
            
            <p className="text-lg">
              I'm passionate about software development and programming. I'm in the early 
              stages of my journey, learning various technologies like HTML5, CSS, JavaScript, 
              Python, C, and Java while building projects to enhance my skills.
            </p>
            
            <p className="text-lg">
              When I'm not coding, you can find me exploring new technologies, reading tech blogs, 
              or working on personal projects. I'm always eager to learn and grow in this field!
            </p>
          </div>
          
          <div>
            <div className="relative">
              <div className="absolute -inset-1 bg-gradient-to-r from-primary to-purple-600 rounded-lg blur opacity-25"></div>
              <div className="relative bg-white rounded-lg overflow-hidden">
                <img 
                  src="https://images.unsplash.com/photo-1560250097-0b93528c311a" 
                  alt="Anupam Baral" 
                  className="w-full h-auto"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default About;
