"use client"

import { useState } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { Button } from "@/components/ui/button"
import { Card, CardContent } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { Moon, Sun, Code, User, Briefcase, Mail, Zap, Database, Cloud, Home, Info, FolderOpen, Send } from "lucide-react"

export default function MinimalistPortfolio() {
  const [activeSection, setActiveSection] = useState("home")
  const [isDarkMode, setIsDarkMode] = useState(false)

  const toggleDarkMode = () => {
    setIsDarkMode(!isDarkMode)
    document.documentElement.classList.toggle("dark")
  }

  const sections = [
    { id: "home", icon: Home },
    { id: "about", icon: Info },
    { id: "projects", icon: FolderOpen },
    { id: "contact", icon: Send }
  ]

  const projectsData = [
    { title: "E-commerce Platform", description: "Full-stack solution with React and Node.js" },
    { title: "Task Manager", description: "Kanban-style app with drag-and-drop functionality" },
    { title: "Weather Dashboard", description: "Real-time weather data visualization" },
  ]

  return (
    <div className={`min-h-screen ${isDarkMode ? "dark" : ""}`}>
      <div className="bg-[#f0f4f8] dark:bg-[#1a202c] min-h-screen text-[#2d3748] dark:text-[#e2e8f0] transition-colors duration-300">
        <nav className="container mx-auto p-4 border-b border-[#cbd5e0] dark:border-[#4a5568]">
          <div className="flex justify-between items-center">
            <motion.div 
              className="flex items-center space-x-2"
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.5 }}
            >
              <Zap className="h-8 w-8 text-black dark:text-white" />
              <h1 className="text-2xl font-bold">Minimalist Portfolio</h1>
            </motion.div>
            <div className="flex space-x-4">
              {sections.map((section) => (
                <Button
                  key={section.id}
                  variant="ghost"
                  onClick={() => setActiveSection(section.id)}
                  className={`text-[#4a5568] dark:text-[#a0aec0] ${activeSection === section.id ? "bg-[#edf2f7] dark:bg-[#2d3748]" : ""}`}
                >
                  <section.icon className="mr-2 h-4 w-4" />
                  {section.id.charAt(0).toUpperCase() + section.id.slice(1)}
                </Button>
              ))}
              <Button variant="outline" size="icon" onClick={toggleDarkMode}>
                {isDarkMode ? <Sun className="h-4 w-4" /> : <Moon className="h-4 w-4" />}
              </Button>
            </div>
          </div>
        </nav>

        <main className="container mx-auto p-4">
          <AnimatePresence mode="wait">
            <motion.div
              key={activeSection}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              transition={{ duration: 0.5 }}
            >
              {activeSection === "home" && (
                <motion.div 
                  className="text-center py-20"
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.5 }}
                >
                  <Avatar className="w-32 h-32 mx-auto mb-8">
                    <AvatarImage src="/placeholder.svg" alt="Profile Picture" />
                    <AvatarFallback>JD</AvatarFallback>
                  </Avatar>
                  <h2 className="text-5xl font-bold mb-4 text-[#2d3748] dark:text-[#e2e8f0]">
                    Welcome to My Minimalist World
                  </h2>
                  <p className="text-xl mb-8 text-[#4a5568] dark:text-[#a0aec0]">Crafting clean, efficient, and innovative digital solutions</p>
                  <Button onClick={() => setActiveSection("projects")} size="lg" className="bg-black hover:bg-gray-800 text-white">
                    Explore My Work
                  </Button>
                </motion.div>
              )}

              {activeSection === "about" && (
                <motion.div
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.5 }}
                >
                  <Card className="bg-white dark:bg-[#2d3748] shadow-lg">
                    <CardContent className="p-6">
                      <div className="flex items-center mb-6">
                        <Avatar className="w-24 h-24 mr-6">
                          <AvatarImage src="/placeholder.svg" alt="Profile Picture" />
                          <AvatarFallback>JD</AvatarFallback>
                        </Avatar>
                        <div>
                          <h2 className="text-3xl font-bold mb-2 text-[#2d3748] dark:text-[#e2e8f0]">About Me</h2>
                          <p className="text-[#4a5568] dark:text-[#a0aec0]">Full-stack Developer | UI/UX Enthusiast</p>
                        </div>
                      </div>
                      <p className="mb-4 text-[#4a5568] dark:text-[#a0aec0]">
                        I'm a passionate full-stack developer with a keen eye for minimalist design and a love for creating
                        efficient, user-friendly experiences. My expertise spans React, Node.js, and cloud technologies,
                        allowing me to bring ideas to life with clean, scalable code.
                      </p>
                      <div className="grid grid-cols-2 gap-4">
                        <div className="flex items-center text-[#4a5568] dark:text-[#a0aec0]">
                          <Code className="mr-2 text-black dark:text-white" /> Frontend Development
                        </div>
                        <div className="flex items-center text-[#4a5568] dark:text-[#a0aec0]">
                          <Database className="mr-2 text-black dark:text-white" /> Backend Development
                        </div>
                        <div className="flex items-center text-[#4a5568] dark:text-[#a0aec0]">
                          <User className="mr-2 text-black dark:text-white" /> UI/UX Design
                        </div>
                        <div className="flex items-center text-[#4a5568] dark:text-[#a0aec0]">
                          <Cloud className="mr-2 text-black dark:text-white" /> Cloud Deployment
                        </div>
                      </div>
                    </CardContent>
                  </Card>
                </motion.div>
              )}

              {activeSection === "projects" && (
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                  {projectsData.map((project, index) => (
                    <motion.div
                      key={index}
                      initial={{ opacity: 0, y: 20 }}
                      animate={{ opacity: 1, y: 0 }}
                      transition={{ duration: 0.5, delay: index * 0.1 }}
                    >
                      <Card className="bg-white dark:bg-[#2d3748] shadow-lg h-full">
                        <CardContent className="p-6 flex flex-col h-full">
                          <Briefcase className="mb-2 text-black dark:text-white" />
                          <h3 className="text-xl font-bold mb-2 text-[#2d3748] dark:text-[#e2e8f0]">{project.title}</h3>
                          <p className="flex-grow text-[#4a5568] dark:text-[#a0aec0]">{project.description}</p>
                          <Button className="mt-4 bg-black hover:bg-gray-800 text-white">View Project</Button>
                        </CardContent>
                      </Card>
                    </motion.div>
                  ))}
                </div>
              )}

              {activeSection === "contact" && (
                <motion.div
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.5 }}
                >
                  <Card className="bg-white dark:bg-[#2d3748] shadow-lg max-w-md mx-auto">
                    <CardContent className="p-6">
                      <h2 className="text-3xl font-bold mb-4 text-[#2d3748] dark:text-[#e2e8f0]">Get in Touch</h2>
                      <form className="space-y-4" onSubmit={(e) => e.preventDefault()}>
                        <div>
                          <label htmlFor="name" className="block mb-1 text-[#4a5568] dark:text-[#a0aec0]">Name</label>
                          <Input id="name" placeholder="Your name" className="bg-[#edf2f7] dark:bg-[#4a5568] border-[#cbd5e0] dark:border-[#718096]" />
                        </div>
                        <div>
                          <label htmlFor="email" className="block mb-1 text-[#4a5568] dark:text-[#a0aec0]">Email</label>
                          <Input id="email" type="email" placeholder="Your email" className="bg-[#edf2f7] dark:bg-[#4a5568] border-[#cbd5e0] dark:border-[#718096]" />
                        </div>
                        <div>
                          <label htmlFor="message" className="block mb-1 text-[#4a5568] dark:text-[#a0aec0]">Message</label>
                          <Textarea id="message" placeholder="Your message" className="bg-[#edf2f7] dark:bg-[#4a5568] border-[#cbd5e0] dark:border-[#718096]" />
                        </div>
                        <Button className="w-full bg-black hover:bg-gray-800 text-white">Send Message</Button>
                      </form>
                    </CardContent>
                  </Card>
                </motion.div>
              )}
            </motion.div>
          </AnimatePresence>
        </main>

        <footer className="container mx-auto p-4 text-center mt-8 text-[#4a5568] dark:text-[#a0aec0] border-t border-[#cbd5e0] dark:border-[#4a5568]">
          <p>&copy; 2023 Minimalist Portfolio. All rights reserved.</p>
        </footer>
      </div>
    </div>
  )
}